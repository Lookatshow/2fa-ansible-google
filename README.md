# 2fa-ansible-google
Google Authenticator with Ansible


<b>Для запуска playbook:</b>

      
      `ansible-palybook playbook-name`


<b>Операции с пользователями и ключами:</b>


1) <b>Создание нескольких пользователей</b>В переменных, находящихся в папке vars - необходимо указать пользователей users:  или user: и внести правки в переменную в task'e user
  
      
      `ansible-playbook user-create.yml`
      
      
 2) <b>Удаление пользователя или нескольких пользователей</b> В переменных, находящихся в папке vars - необходимо указать пользователей users:  или user: и внести правки в переменную в task"e user/uesr

      
      `ansible-playbook user-delete.yml`
 
 
 3) <b>Изменение нескольких пользователей</b>


      
      `ansible-playbook user-change.yml`       
       
       
 4) <b>Добавление пользователя в группу</b>

      
      `ansible-playbook user-add-to-group.yml`



 5) <b>Изменение пользователя или нескольких пользователей</b>

      
      `ansible-playbook user-change.yml`


6) <b>Создание sudo-пользователей</b>
Используется задание roles/2FA/tasks/users.yml
Переменная с именем пользователя - должна лежать в vars/main.yml user_name, 
  
      
      `ansible-playbook users.yml -i hosts.yml`


# Установка инастройка Google authenticator

Правильной практикой здесь будет использование Inverntory файла Ansible + Ad-Hoc команд с плейбуками для универсальной раскатки в зависимости от ОС (например в weezy репе нет libpam-google-authenticator). Но в текущей ситуации юзаем под ubuntu 20.04

<b>Для установки и конфигурации Google Authenticator - необходимо запустить плейбук:</b>
Nullok - даёт возможность первого входа без 2FA и его настройки (подкинул скрипт .sh но не доработал, нужно проверять первый вход пользователя и запускать google-authenticator утилиту, это не оч правильно, лучше написать systemd unit)

`ansible-playbook oogle-authenticator-install-configure.yml`

<b>Для отклчения Google Authenticator - необходимо запустить плейбук:</b>


`ansible-playbook google-authenticator-disable.yml`


# Доставка private.key и QR-code Google Authenticator пользовтелям машин

<b>Если в организации есть SMTP Relay - можем прикрутить скрипт для рассылки информации по созаднным пользователям (ссылка на QR-Code и private.key) </b>

      `python3 sendKeyToUser UserName /path/Private.key`

Так же можно переделать под шаринг через PasswordManager если у него есть API



# Hardening SSH - Установка и конфигурирование fail2ban на хостах 

- Настройка fail2ban
- Внешний контроль Weak Encryption (для хешей) или ограничение доступа толкьо с доверенных подсетей (ufw.yml)

`ansible-playbook ufw.yml`

(Максимум паранойи)
Захарденить ближайший маршрутизатор, во избежание - BGP Hijacking.

Параметры Cisco :
- bgp log neighbour changes, - bgp neighbour <ip> (сессия строго с это железкой),
- аутентификация сессии
- следить за уязвимостями( железки inventory + vm, патчить сложно, конечно, но так, на всякий)
- Ограничить список адресов и маршрутов которые могут анонсировать и могут быть анонсированы
