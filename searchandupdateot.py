import time
import pyautogui
from time import sleep
import pyperclip
import pendulum
from storagefunctions import (pressingKey,make_window_visible)

def searchOTHControl(incidentId):
    
    crm_otp_saved_sucessfully = crm_save_incident = crm_assign_user = crm_edit_incident = aliado_implementacion_field = aliado_implementacion_field2 = crm_dashboard = crm_warning_message = crm_ot_blocked_message = mod_consulta_popup = None 
    crmAttempts = 0  

    #/////////////////////////////////// CRM DASHBOARD ///////////////////////////////////////////    

    while crm_dashboard is None:
        crm_dashboard = pyautogui.locateOnScreen('C:/Cambio de Items/assets/crm_dashboard.png', grayscale = True,confidence=0.85)
        sleep(0.5)
        if crmAttempts == 5:
            pyautogui.getWindowsWithTitle("Sistema Avanzado de Administración de Clientes [Versión 4.2.2.3]")[0].minimize()
            pyautogui.getWindowsWithTitle("Sistema Avanzado de Administración de Clientes [Versión 4.2.2.3]")[0].maximize()
            print("Estoy dentro de los 5 intentos para ver el Dashboard del CRM")
            crmAttempts = 0
        crmAttempts = crmAttempts + 1
                
    print("CRM Dashboard GUI is present!")   
    pyautogui.click(pyautogui.center(crm_dashboard))    
    
    sleep(0.5)
    pressingKey('f2')
    while mod_consulta_popup is None:        
        mod_consulta_popup = pyautogui.locateOnScreen('C:/Cambio de Items/assets/mod_consulta_popup.png', grayscale = True,confidence=0.85)            
        pressingKey('f2')
    print("mod_consulta_popup field is present and detected on GUI screen!")
    sleep(0.5)
    pyautogui.write(incidentId)
    sleep(0.5)
    pressingKey('enter')
    pressingKey('enter')
    
    #/////////////////////////////////// FASE DE INGRESO ///////////////////////////////////////////
    
    while crm_ot_blocked_message is None and crm_warning_message is None and crmAttempts < 10:
        crm_warning_message = pyautogui.locateOnScreen('C:/Cambio de Items/assets/mensaje_advertencia.png', grayscale = True,confidence=0.9)   
        crm_ot_blocked_message = pyautogui.locateOnScreen('C:/Cambio de Items/assets/crm_ot_blocked_message.png', grayscale = True,confidence=0.9)   
        sleep(0.5)
        if crmAttempts == 8:
            print("Estoy dentro de los 8 intentos de medio seg para esperar algun pop up de OT bloqueada inesperado en el CRM")                        
        crmAttempts += 1
        print(crmAttempts)            

    if(crm_ot_blocked_message is None and crm_warning_message is None):
        print("No se encuentrarn ventanas de advertencia!")                           
        
        # Validate edit_incident view is visible and on focus            
        while crm_edit_incident is None:
            crm_edit_incident = pyautogui.locateOnScreen('C:/Cambio de Items/assets/edit_incident.png', grayscale = True,confidence=0.9)   
        print("Vista de Detalles is present!")    
        print("CRM Edit Incident button is present!")
        crm_edit_incident_x,crm_edit_incident_y = pyautogui.center(crm_edit_incident)
        pyautogui.click(crm_edit_incident_x, crm_edit_incident_y)
    
        # Validate assign user pop up is visible and on focus
        # crm_assign_user = None  # reset variable   
        crmAttempts = 0
        while crm_assign_user is None and crmAttempts < 5:
            crm_assign_user = pyautogui.locateOnScreen('C:/Cambio de Items/assets/asignar_ot_usuario_operador.png', grayscale = True,confidence=0.9)   
            sleep(0.5)
            print("buscando ventana de asignación de usuario")
            crmAttempts +=1            
        if crm_assign_user is not None:
            print("CRM Confirm Assign Pop Up is present!")
            sleep(1)
            pressingKey('n') # No re asignar usuario al momento de editar las OTPs 
            sleep(1)
    
    # ------- ACCIONES FASE DE ADVERTENCIA --------
    else:
        pressingKey('enter')
        sleep(3)
        pressingKey('enter')
        sleep(1)
        pyautogui.hotkey('alt','f4')
        return 9
    
    # Maximize CRM window 
    pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].maximize()
    print("CRM Edit view Window was maximized!")    
    # Click on open Details Button on the CRM to make date fields visible    
    pyautogui.click(20,496)
    crmAttempts = 0
    
    #/////////////////////////////////// UPDATE BILLING ITEM  /////////////////////////////////////  
    # Identify which UI is present on screen. Then focus on BILLING ITEM FIELD and select the incoming billing item 

    scrollTimes = 0
    pyautogui.moveTo(267, 514)    
    while aliado_implementacion_field is None and scrollTimes <= 300:
        pyautogui.scroll(-15)
        sleep(0.03)
        print("buscando aliado_implementacion_field in screen")
        aliado_implementacion_field = pyautogui.locateOnScreen('C:/Cambio de Items/assets/aliado_implementacion.png', grayscale = True,confidence=0.95)        
    if aliado_implementacion_field is not None:
        Estado_OTH_x,Estado_OTH_y = pyautogui.center(aliado_implementacion_field)
        pyautogui.click(Estado_OTH_x,Estado_OTH_y)  
        posicion_actual = pyautogui.position()
        print("Posición actual del cursor:", posicion_actual)
        # Mover el cursor 127 píxeles a la derecha desde su posición actual
        pyautogui.moveRel(183, 0, duration=0.5)
        # Imprimir la nueva posición del cursor
        nueva_posicion = pyautogui.position()
        print("Nueva posición del cursor:", nueva_posicion)
        pyautogui.doubleClick(nueva_posicion)
        sleep(1)

    if(scrollTimes > 299):
        print("billing item field was not found on GUI screen!")    
    else:
        print("billing item field is present and detected on GUI screen!")      

    sleep(1)    
    pyautogui.write("NAE")
    pressingKey("enter")
    pressingKey('tab')
    pyautogui.write("NAE")
    pressingKey("enter")
    sleep(1)
    
    #/////////////////////////////////// CLOSING PHASE /////////////////////////////////////    
    
    while crm_save_incident is None:
        crm_save_incident = pyautogui.locateOnScreen('C:/Cambio de Items/assets/guardar_incidente_button.png', grayscale = True,confidence=0.9)   
    print("CRM Save Incident button is present!")
    crm_save_incident_x,crm_save_incident_y = pyautogui.center(crm_save_incident)
    pyautogui.click(crm_save_incident_x, crm_save_incident_y)   
    
    sleep(1)    
    crm_assign_user = None
    while crm_warning_message is None and crm_assign_user is None:  
        print("buscando o crm_warning_message o crm_assign_user")      
        crm_warning_message = pyautogui.locateOnScreen('C:/Cambio de Items/assets/mensaje_advertencia.png', grayscale = True,confidence=0.9)   
        crm_assign_user = pyautogui.locateOnScreen('C:/Cambio de Items/assets/asignar_ot_usuario_operador.png', grayscale = True,confidence=0.9)   
        sleep(0.5)                
        
    if(crm_warning_message is None):
        print("CRM empty_warning_message_crm pop up is not present!")
                
        # Validate assign user pop up is visible and on focus   
        crm_assign_user = None  # reset variable
        crmAttempts = 0
        while crm_assign_user is None and crmAttempts < 5:
            crm_assign_user = pyautogui.locateOnScreen('C:/Cambio de Items/assets/asignar_ot_usuario_operador.png', grayscale = True,confidence=0.9)   
            sleep(0.5)
            print("buscando ventana de asignación de usuario")            
            crmAttempts +=1            
        if crm_assign_user is not None:
            print("CRM Confirm Assign Pop Up is present!")
            sleep(1)
            pressingKey('n') # No re asignar usuario al momento de editar las OTPs 
            sleep(1)

        # Validate save OTP successfully  pop up is visible and on focus   
        while crm_otp_saved_sucessfully is None:
            crm_otp_saved_sucessfully = pyautogui.locateOnScreen('C:/Cambio de Items/assets/incidente_guardado_exitosamente.png', grayscale = True,confidence=0.9)   
        print("CRM OTP Saved Succesfully Pop Up is present!")
        sleep(1)
        pressingKey('enter')
        sleep(1)

        # Validate if changes must be saved or not and Close the OT Details View On Edition mode  
        # Close Edit Incident View 
        pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
        sleep(1.5)
        return 0
    else:
        print("CRM empty_warning_message_crm pop up is present!")
        #pyautogui.click(pyautogui.center(crm_warning_message))
        sleep(0.5)
        pressingKey('enter')
        sleep(1)
        pressingKey('enter')
        sleep(1)
        pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
        sleep(1)
        pressingKey('n')        
            
        return 9