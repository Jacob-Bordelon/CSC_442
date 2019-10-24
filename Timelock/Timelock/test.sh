for i in {0..9}
do
	echo "============================="
	echo "test $i"
	python test.py $i
	echo "============================="
done
