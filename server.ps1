try {
    wt nt --title 'Django Server' -d ./hotel_management_system powershell -noExit 'py .\manage.py runserver' `; nt --title 'LiveReload Server' -d ./hotel_management_system powershell -noExit "py .\manage.py livereload" `; nt --title 'TailwindCSS Server' -d ./hotel_management_system powershell -noExit "npx tailwindcss -i .\static\css\styles.css -o .\static\dist\output.css --watch" `; focus-tab -t 0
}
catch {

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
}
