for f in `cat tables.txt` ; do
	echo "class $f ():" > $f.class.py
done

# user
# user_role
# hierarchy_lvl
# hierarchy_role
# permission
