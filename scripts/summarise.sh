#!/bin/bash
# Purpose: Summarises availability monitor logs including distinct version counts.
# Usage: ./scripts/summarise.sh evidence/e4.1-at-rest-log.txt

LOG_FILE=${1:-"evidence/e4.1-at-rest-log.txt"}

if [ ! -f "$LOGF_ILE" ] && [ ! -f "$LOG_FILE" ]; then
    echo "Log file $LOG_FILE not found!"
    exit 1
fi

TOTAL=$(wc -l < "$LOG_FILE")
OK_COUNT=$(grep -c " OK " "$LOG_FILE")
FAIL_COUNT=$(grep -c " FAIL " "$LOG_FILE")
START_TIME=$(head -n 1 "$LOG_FILE" | awk '{print $1}')
END_TIME=$(tail -n 1 "$LOG_FILE" | awk '{print $1}')

echo "=== Availability Log Summary ==="
echo "Log File:         $LOG_FILE"
echo "Start Timestamp:  $START_TIME"
echo "End Timestamp:    $END_TIME"
echo "Total Requests:   $TOTAL"
echo "Successful (OK):  $OK_COUNT"
echo "Failed (FAIL):    $FAIL_COUNT"
echo ""
echo "=== Version Counts ==="
grep " OK " "$LOG_FILE" | grep -o '"version": *"[^"]*"' | sort | uniq -c
echo "================================"