from . import comercio, ia

# Orden: por tema y, dentro de cada tema, por mirada
BUILDERS = [*ia.BUILDERS, *comercio.BUILDERS]
