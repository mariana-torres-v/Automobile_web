Feature: Navegación y validación de UI del sitio Digital-ByKon Consulting

  Scenario: Carga exitosa de la página principal
    Given que el usuario navega a la URL de "Digital-ByKon Consulting"
    Then la página principal se debe abrir y visualizar correctamente

  Scenario: Acceso al Aviso de Privacidad mediante scroll
    Given que el usuario se encuentra en la página principal de "Digital-ByKon Consulting"
    When hace swipe o scroll hasta el final de la página
    And da clic en el enlace "Privacy notice"
    Then la página de Aviso de Privacidad se debe abrir correctamente

  Scenario: Navegación a la sección de Servicios Digitales
    Given que el usuario se encuentra en el menú principal
    When ingresa a la opción "Services"
    And selecciona "Digital"
    Then la página de la sección "Services > Digital" se debe abrir correctamente

  Scenario: Apertura del modal para agendar una llamada
    Given que el usuario se encuentra en la página de "Services > Digital"
    When da clic en el botón "Book a call"
    Then se debe abrir correctamente el modal para agendar una llamada

  Scenario: Validación de diseño al traducir la página
    Given que el usuario se encuentra en la página de "Services > Digital"
    When traduce el contenido de la página al español mediante Google Translate
    Then el texto de la página se debe leer en español
    And los elementos de texto no deben encimarse ni romper el diseño