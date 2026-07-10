Feature: Navegación y validación de UI del sitio Digital-ByKon Consulting

  # Step que se ejecuta antes de cada escenario
  Background:
    Given que el usuario se encuentra en la página principal de "Digital-ByKon Consulting"

  Scenario: Carga exitosa de la página principal
    Then la página principal se debe abrir y visualizar correctamente

  Scenario: Acceso al Aviso de Privacidad mediante scroll
    When el usuario hace scroll hasta el botón "Aviso de Privacidad"
    And el usuario da clic en el botón "Aviso de Privacidad"
    Then el sistema abre la página de Aviso de Privacidad

  Scenario: Navegación a la sección de Servicios Digitales
    When el usuario hace hover sobre "Services"
    And el usuario da clic en "Digital"
    Then el sistema abre la página de la sección "Services > Digital"

  Scenario: Apertura del modal para agendar una llamada
    When el usuario da clic en el botón "Book a call"
    Then el sistema redirige a la página para agendar una llamada

  Scenario: Validación de diseño al traducir la página nativo de Google
    When el usuario da clic en el botón de google para traducir el contenido de la página
    Then el sistema muestra el texto de la página en español
    And el sistema en español no encima los elementos ni rompe el diseño

  Scenario: Validación de diseño al traducir la página
    When el usuario da clic en la bandera de México
    Then el sistema muestra el texto de la página en español
    And el sistema en español no encima los elementos ni rompe el diseño
