invoke-expression 'cmd /c start powershell -NoExit -Command { 
    dbms_cp/Scripts/activate;
    cd ./hotel_management_system;
    cls; 
    py .\manage.py livereload; 
    $host.UI.RawUI.WindowTitle = "Django Live Reload Server"; 

}';
invoke-expression 'cmd /c start powershell -NoExit -Command { 
    dbms_cp/Scripts/activate;
    cd ./hotel_management_system;
    cls; 
    start-process chrome;
    py .\manage.py runserver; 
    $host.UI.RawUI.WindowTitle = "Django Server"; 
}';

invoke-expression 'cmd /c start powershell -NoExit -Command { 
    dbms_cp/Scripts/activate;
    cd ./hotel_management_system;
    cls; 
    npx tailwindcss -i ./static/css/styles.css -o ./static/dist/output.css --watch; 
    $host.UI.RawUI.WindowTitle = "TailwindCSS server"; 
}';