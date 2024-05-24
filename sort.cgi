#!/bin/bash

saveIFS=$IFS
IFS='=&'
parm=($QUERY_STRING)
IFS=$saveIFS

echo "Content-type: text/html"
echo ""
echo ""
echo "<html>"
echo "<head><title>Sort Text</title></head>"
echo "<body>"
echo "<h1>Enter text to  be manipulated like a narcissist their victim:</h1>"
echo "<form action='sort.cgi' method='put'>"
echo "<textarea name='text' rows='10' cols='100'></textarea><br>"
echo "<input type='submit' value='Sort Text'>"
echo "</form>"

sorted_text=$(echo "$QUERY_STRING" | cut -c 6- )
sorted_text=$(echo "$sorted_text" | sed 's/%0D%0A/\n/g')

sorted_text2=$(echo "$sorted_text" | sort )

# Print the sorted text as the output
echo "<br>"
echo "Before processing:"
echo "<br>"
echo "<pre>"
echo "$sorted_text"
echo "</pre>"
echo "<br>"
echo "After processing:"
echo "<br>"
echo "<pre>"
echo "$sorted_text2"
echo "</pre>"
echo "</body>"
echo "</html>"
exit 0
