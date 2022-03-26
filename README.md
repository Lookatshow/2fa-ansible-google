# 2fa-ansible-google
Google Authenticator with Ansible


<b>Для запуска playbook:</b>

      
      `ansible-palybook playbook-name`


1) <b>Создание нескольких пользователей</b>
В переменных, находящихся в папке vars - необходимо указать пользователей users:  или user: и внести правки в переменную в task"e user/uesr
  
      
      `ansible-playbook user-create.yml`
      
      
 2) <b>Удаление пользователя или нескольких пользователей</b>

В переменных, находящихся в папке vars - необходимо указать пользователей users:  или user: и внести правки в переменную в task"e user/uesr

      
      `ansible-playbook user-delete.yml`
 
 
 3) <b>Изменение нескольких пользователей</b>


      
      `ansible-playbook user-change.yml`
       
       
       
 4) <b>Добавление пользователя в группу</b>

      
      `ansible-playbook user-add-to-group.yml`



 5) <b>Изменение пользователя или нескольких пользователей</b>

      
      `ansible-playbook user-change.yml`


6) <b>Создание sudo-пользователей</b>
Используется задание roles/2FA/tasks/user.yml
Переменная с именем пользователя - должна лежать в vars/main.yml user_name, 
  
      
      `ansible-playbook user-sudo-create.yml`


<b>Если в организации есть SMTP Relay - можем прикрутить скрипт для рассылки информации по созаднным пользователям (ссылка на QR-Code и private.key) </b>
