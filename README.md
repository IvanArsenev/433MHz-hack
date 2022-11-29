### Languages and Tools:
<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />
<img align="left" alt="Python" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/raspberry-pi/raspberry-pi.png" />
<img align="left" alt="Visual Studio Code" width="26px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png"/><br/><br/>

<h2># WORKING WITH 433MHz TRANSMITTERS WITH RASPBERRY PI</h2>
<h2>Инструкция на русском ниже</h2>

Modern barriers, electronic gates, and some electronic locks operate on these frequencies. By reading the values from the receiver when there is a signal from the remote control to open something, you can repeat this signal, thereby opening/closing the target.

<h2>The following types of modules are used for receiving and transmitting:</h2>

![alt text](https://static-sl.insales.ru/images/products/1/1171/141264019/1070.jpg)
![alt text](https://ae01.alicdn.com/kf/HTB1day5aULrK1Rjy1zbq6AenFXa6/QIACHIP-433-Mhz.jpg)

<h2>I connected them according to the scheme:</h2>

![alt text](https://github.com/EternalB-1/rf/blob/master/img/Screenshot_1.png?raw=true)

<h3>After that, you need to install the library and repository:</h3>

git clone https://github.com/EternalB-1/rf_ru

pip3 install rpi-rf

<h3>If you have any problems installing the rpi-rf library, there is a folder with it in the repository. To install it manually, enter:</h3>

cd rf/rpi-rf-0.9.6

sudo python3 setup.py install

<h2>To receive a signal, enter:</h2>

cd rf

python3 recieve.py -g 20

<h2>To send a signal (if you receive a signal at this time, create a new session):</h2>

cd rf

python3 send.py -g 21 -t * -p ** ***

*- protocol

**-pulse

***- device code

=========================================================

<h2># РАБОТА С ПЕРЕДАТЧИКАМИ 433 МГц С RASPBERRY PI</h2>

На этих частотах работают современные шлагбаумы, электронные ворота и некоторые электронные замки. Считывая значения с приемника при поступлении сигнала с пульта дистанционного управления на открытие чего-либо, вы можете повторить этот сигнал, тем самым открывая/закрывая цель.

<h2>Для приема и передачи используются следующие типы модулей:</h2>

![alt text](https://static-sl.insales.ru/images/products/1/1171/141264019/1070.jpg)
![alt text](https://ae01.alicdn.com/kf/HTB1day5aULrK1Rjy1zbq6AenFXa6/QIACHIP-433-Mhz.jpg)

<h2>Я соединил их по схеме:</h2>

![alt text](https://github.com/EternalB-1/rf/blob/master/img/Screenshot_1.png?raw=true)

<h3>После этого вам нужно установить репозиторий и библиотеку:</h3>

git clone https://github.com/EternalB-1/rf_ru

pip3 установка rpi-rf

<h3>Если у вас возникли проблемы с установкой библиотеки rpi-rf, то в репозитории есть папка с ней. Чтобы установить его вручную, введите:</h3>

cd rf/rpi-rf-0.9.6

sudo python3 setup.py установка

<h2>Чтобы получить сигнал, введите:</h2>

cd rf

python3 recieve.py -g 20

<h2>Для отправки сигнала (если вы получаете сигнал в это время, создайте новый сеанс):</h2>

cd rf

python3 send.py -g 21 -t * -p ** ***

*- протокол

**-пульс

***- код устройства
