change pi password
edit /etc/hosts and etc/hostname to change to hat name

edit /etc/fstab, add:
tmpfs /var/ipc  tmpfs defaults,noatime,size=16m 0 0


 sudo apt-get install \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     software-properties-common

$ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

echo "deb [arch=armhf] https://download.docker.com/linux/debian \
     $(lsb_release -cs) stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list

    