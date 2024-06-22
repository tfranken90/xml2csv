~/go/bin/yambs -type recording \
	-format csv \
	-fields rel0_attr0_text,name,length,disambiguation,url0_url \
	-set url0_type=255 \
	-set rel0_type=740 \
	-set rel0_attr0_type=a59c5830-5ec7-38fe-9a21-c7ea54f6650a \
	-set 'artist0_join= with ' \
	-set artist0_mbid=b9646755-755d-4d88-916f-e9ff90c35473 \
	-set rel0_target=8f060afe-182c-41d0-8fd5-b881cb41de80 \
	-set edit_note="Generated from https://rss.art19.com/sean-carrolls-mindscape" \
	out.csv

#	-set 'artist0_join= & ' \
#	-set artist1_mbid=e2f4cf86-41ac-4591-ad02-ceb4ea2d87ef \
