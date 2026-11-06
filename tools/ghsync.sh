#!/bin/bash
# Copy the website source into the GitHub working copy (no secrets, no build output)
S=/tmp/claude-0/-home-claude/35c3f5ad-aa3e-5285-ae81-3a4fa777bc81/scratchpad; R=/home/claude/adsncodes-website
rm -rf $R/site2 && cp -a $S/site2 $R/site2 && find $R/site2 -name __pycache__ -prune -exec rm -rf {} +
mkdir -p $R/server $R/tools
cp $S/prod/.htaccess $S/prod/audit.php $R/server/
cp $S/mkprod.py $R/
cp $S/up.sh $S/seoaudit.py $S/qa.js $S/ghsync.sh $R/tools/
