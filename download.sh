# download_url="https://universe.roboflow.com/ds/Rip3EJ32nf?key=cm3oHddT5K"
# download_url="https://universe.roboflow.com/ds/mz4oxWcyxg?key=pxefKV1pRR"
# download_url="https://universe.roboflow.com/ds/c3qj4K7y2p?key=rTUKI62mJJ"
# download_url="https://universe.roboflow.com/ds/cO7kQqQ7bJ?key=SGMrn3lhK4"


# download_url="https://universe.roboflow.com/ds/ZP7hqIy1iL?key=0VeFblTtjo"
# download_url="https://universe.roboflow.com/ds/IdQlLDpSq2?key=FUpZWRChFb"
# download_url="https://universe.roboflow.com/ds/HKkcQrb8mK?key=O2EEVXNmHK"
# download_url="https://universe.roboflow.com/ds/XhuCj9xWS9?key=wiuYH0TFE5"

# TODO
download_url="https://universe.roboflow.com/ds/R78UIyJdUP?key=gmBml7Ujec"
download_url="https://universe.roboflow.com/ds/U8yb17DMXL?key=6HeXqJsROt"
download_url="https://universe.roboflow.com/ds/oiegE9vNyx?key=siZweTxi6T"

max_dir_num=$(ls -d datasets/*/ | xargs -I {} basename {} | sort -n | tail -n 1 | sed 's/^0*//')
new_dir_num=$(($max_dir_num + 1))
new_dir_name=datasets/$(printf "%03d" $new_dir_num)
echo "will mkdir $new_dir_name and unzip to it"
mkdir -p $new_dir_name

curl -L $download_url > roboflow.zip; unzip -q roboflow.zip -d $new_dir_name; rm roboflow.zip

echo "done"