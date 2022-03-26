# 2fa-ansible-google
Google Authenticator with Ansible


Для запуска playbook:

      
      `ansible-palybook playbook-name`


1) Создание нескольких пользователей
В переменных, находящихся в папке vars - необходимо указать пользователей users:  или user: и внести правки в переменную в task"e user/uesr
  
      
      `ansible-playbook user-create.yml`
      
      
 2) Удаление пользователя или нескольких пользователей

В переменных, находящихся в папке vars - необходимо указать пользователей users:  или user: и внести правки в переменную в task"e user/uesr

      
      `ansible-playbook user-delete.yml`
 
 
 3) Изменение нескольких пользователей


      
      `ansible-playbook user-change.yml`
       
       
       
 4) Добавление пользователя в группу

      
      `ansible-playbook user-add-to-group.yml`



 5) Изменение пользователя или нескольких пользователей

      
      `ansible-playbook user-change.yml`


6) Создание sudo-пользователей
Используется задание roles/2FA/tasks/user.yml
Переменная с именем пользователя - должна лежать в vars/main.yml user_name, 
  
      
      `ansible-playbook user-sudo-create.yml`


<b>Если в организации есть SMTP Relay - можем прикрутить скрипт для рассылки информации по созаднным пользователям (ссылка на QR-Code и private.key) </b>
