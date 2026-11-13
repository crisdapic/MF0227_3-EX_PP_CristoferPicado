class EstadoInvalidoError(Exception):
    """Excepción personalizada para manejar transiciones de estado no permitidas."""
    pass


class TicketTecnico:
    """Clase base que representa un ticket técnico aplicando POO."""
    
    ESTADOS_VALIDOS = ["Abierto", "En Proceso", "Cerrado"]

    def __init__(self, ticket_id, titulo, prioridad="Media"):
        self._id = ticket_id
        self._titulo = titulo
        self._estado = "Abierto"  # Estado inicial por defecto
        self._prioridad = prioridad

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def estado(self):
        return self._estado

    @property
    def prioridad(self):
        return self._prioridad

    def cambiar_estado(self, nuevo_estado):
        """Método con lógica de negocio para validar y transicionar estados."""
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            raise EstadoInvalidoError(f"El estado '{nuevo_estado}' no existe en el sistema.")

        # Regla de negocio: No se puede pasar de Cerrado a En Proceso ni reabrir directamente
        if self._estado == "Cerrado" and nuevo_estado in ["En Proceso", "Abierto"]:
            raise EstadoInvalidoError(f"Transición no permitida: no se puede cambiar de 'Cerrado' a '{nuevo_estado}'.")

        self._estado = nuevo_estado
        print(f"-> Estado del ticket #{self._id} actualizado exitosamente a: {self._estado}")

    def calcular_sla(self):
        """Método polimórfico base que debe ser implementado por las clases hijas."""
        raise NotImplementedError("Las clases hijas deben implementar el cálculo de SLA.")


class TicketHardware(TicketTecnico):
    """Clase hija para incidencias de Hardware (Herencia)."""

    def __init__(self, ticket_id, titulo, prioridad, componente):
        super().__init__(ticket_id, titulo, prioridad)
        self._componente = componente

    @property
    def componente(self):
        return self._componente

    def calcular_sla(self):
        """Polimorfismo: Cálculo de SLA específico para Hardware (en horas)."""
        if self._prioridad.lower() == "alta":
            return 12
        elif self._prioridad.lower() == "media":
            return 24
        return 48


class TicketSoftware(TicketTecnico):
    """Clase hija para incidencias de Software (Herencia)."""

    def __init__(self, ticket_id, titulo, prioridad, sistema_operativo):
        super().__init__(ticket_id, titulo, prioridad)
        self._sistema_operativo = sistema_operativo

    @property
    def sistema_operativo(self):
        return self._sistema_operativo

    def calcular_sla(self):
        """Polimorfismo: Cálculo de SLA específico para Software (en horas)."""
        if self._prioridad.lower() == "alta":
            return 6
        elif self._prioridad.lower() == "media":
            return 18
        return 36


# Bloque de pruebas unitarias y demostración (Requisito UF2404)
if __name__ == "__main__":
    print("=== PRUEBAS UNITARIAS Y DEMOSTRACIÓN DE POO ===")
    
    try:
        # 1. Probar Ticket de Hardware
        print("\n[1] Probando Ticket de Hardware:")
        t_hw = TicketHardware(ticket_id=101, titulo="Falla en fuente de alimentación", prioridad="Alta", componente="Fuente ATX 650W")
        print(f"Ticket ID: {t_hw.id} | Componente: {t_hw.componente} | SLA: {t_hw.calcular_sla()} hrs")
        
        t_hw.cambiar_estado("En Proceso")
        t_hw.cambiar_estado("Cerrado")
        
        # Intentar una transición inválida para comprobar la excepción personalizada
        print("\nIntentando transición inválida (Cerrado -> En Proceso)...")
        t_hw.cambiar_estado("En Proceso")

    except EstadoInvalidoError as e:
        print(f"[ÉXITO - Excepción capturada]: {e}")

    try:
        # 2. Probar Ticket de Software
        print("\n[2] Probando Ticket de Software:")
        t_sw = TicketSoftware(ticket_id=102, titulo="Error 500 en despliegue Django", prioridad="Alta", sistema_operativo="Ubuntu 22.04 LTS")
        print(f"Ticket ID: {t_sw.id} | SO: {t_sw.sistema_operativo} | SLA: {t_sw.calcular_sla()} hrs")
        
        t_sw.cambiar_estado("En Proceso")
        print(f"Estado actual: {t_sw.estado}")

    except EstadoInvalidoError as e:
        print(f"[Error inesperado]: {e}")