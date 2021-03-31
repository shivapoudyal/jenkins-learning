name=$1
city=$2
boolenVar=$3

if [ $boolenVar = true ]; then
    echo "hello $name, welcome to $city"
else
    echo "boolen type must be true"
fi    
#-------------------------------------------- into jenkins -------------------------------------
# name=shiva
# city=frankfurt
# /script-test/script.sh $name $city
