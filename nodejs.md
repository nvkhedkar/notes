# Nodejs notes

## Install latest nodejs on ubuntu
```
sudo npm cache clean -f
sudo npm install -g n
sudo n stable
```
To upgrade to latest version (and not current stable) version, you can use
```
sudo n latest
```
Fix PATH
```
sudo apt-get install --reinstall nodejs-legacy     # fix /usr/bin/node
```
To undo:
```
sudo n rm 6.0.0     # replace number with version of Node that was installed
sudo npm uninstall -g n
```
## Links
(rascal rabbitmq intro)[https://www.cloudamqp.com/blog/how-to-run-rabbitmq-with-nodejs.html]
(book - Enterprise integration patterns)[https://www.enterpriseintegrationpatterns.com/]
