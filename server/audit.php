<?php
// Free marketing audit form handler: emails bd@adsncodes.com and keeps a private backup copy outside public_html.
header('Content-Type: application/json; charset=utf-8');
header('X-Robots-Tag: noindex');
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') { http_response_code(405); echo '{"ok":false}'; exit; }

// spam traps: hidden field filled, or form sent faster than a person could type
if (!empty($_POST['company_site'])) { echo '{"ok":true}'; exit; }
$t = (int)($_POST['t'] ?? 0);
if ($t > 0 && (time() - $t) < 4) { echo '{"ok":true}'; exit; }

function fld($k, $n = 300) {
  $v = isset($_POST[$k]) && is_string($_POST[$k]) ? $_POST[$k] : '';
  $v = trim(strip_tags($v));
  $v = preg_replace('/[\r\n]+/', ' ', $v);
  return mb_substr($v, 0, $n);
}
$name = fld('name', 100); $biz = fld('biz', 150); $web = fld('web', 300);
$phone = fld('phone', 40); $email = fld('email', 150);
$ind = fld('industry', 80); $em = fld('emirate', 40);
$goal = isset($_POST['goal']) && is_string($_POST['goal']) ? mb_substr(trim(strip_tags($_POST['goal'])), 0, 2000) : '';
$areas = [];
if (isset($_POST['areas']) && is_array($_POST['areas'])) foreach ($_POST['areas'] as $a) if (is_string($a)) $areas[] = mb_substr(strip_tags($a), 0, 40);
$okEmail = filter_var($email, FILTER_VALIDATE_EMAIL) ? $email : '';

if ($name === '' || $biz === '' || ($phone === '' && $okEmail === '')) { http_response_code(400); echo '{"ok":false,"error":"missing"}'; exit; }

// simple rate limit: 5 requests per IP per hour
$ip = $_SERVER['REMOTE_ADDR'] ?? '';
$dir = dirname(__DIR__) . '/leads';
if (!is_dir($dir)) @mkdir($dir, 0700, true);
$rl = $dir . '/rl-' . md5($ip) . '.txt';
$hits = array_filter(array_map('intval', @file($rl, FILE_IGNORE_NEW_LINES) ?: []), function ($x) { return $x > time() - 3600; });
if (count($hits) >= 5) { http_response_code(429); echo '{"ok":false,"error":"rate"}'; exit; }
$hits[] = time(); @file_put_contents($rl, implode("\n", $hits), LOCK_EX);

$when = (new DateTime('now', new DateTimeZone('Asia/Dubai')))->format('Y-m-d H:i');
$lines = [
  "New marketing audit request ($when, Dubai time)", '',
  "Name: $name", "Business: $biz", "Website or Instagram: $web",
  "WhatsApp: $phone", "Email: $okEmail", "Industry: $ind", "Emirate: $em",
  'Audit areas: ' . implode(', ', $areas), '', 'Main goal:', $goal, '',
  'Sent from adsncodes.com/free-marketing-audit.html'
];
$body = implode("\r\n", $lines);
$subject = '=?UTF-8?B?' . base64_encode("New audit request from $biz") . '?=';
$headers = "From: Ads n' Codes Website <noreply@srv1666.main-hosting.eu>\r\n" . ($okEmail ? "Reply-To: $okEmail\r\n" : '') . "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\n";
$sent = @mail('bd@adsncodes.com', $subject, $body, $headers);

$row = [$when, $name, $biz, $web, $phone, $okEmail, $ind, $em, implode('; ', $areas), $goal, $sent ? 'mailed' : 'mail_failed'];
$fh = @fopen($dir . '/audit-requests.csv', 'a');
if ($fh) { flock($fh, LOCK_EX); fputcsv($fh, $row); flock($fh, LOCK_UN); fclose($fh); }

echo json_encode(['ok' => true]);
