def beregn_investering(initialbeløb, månedligt_indskud, år):
  """
  Beregner opsparingen pr. måned for en given investering.

  Args:
    initialbeløb: Det initiale investeringsbeløb.
    månedligt_indskud: Det månedlige indskud til investeringen.
    år: Antallet af år der skal investeres.

  Returns:
    En liste med opsparingen pr. måned.
  """

  # Konverterer antallet af år til antallet af måneder.
  måneder = år * 12

  # Initialiserer en liste til at gemme opsparingen.
  opsparing = [initialbeløb]

  # Beregner opsparingen pr. måned.
  for måned in range(1, måneder + 1):
    # Rente beregnes på den opsparing fra forrige måned.
    rente = opsparing[-1] * 0.04 / 12

    # Ny opsparing beregnes som summen af forrige måneds opsparing, rente og månedligt indskud.
    ny_opsparing = opsparing[-1] + rente + månedligt_indskud

    # Tilføjer ny opsparing til listen.
    opsparing.append(ny_opsparing)

  return opsparing

# Spørger brugeren om input.
initialbeløb = float(input("Indtast initialbeløb: "))
månedligt_indskud = float(input("Indtast månedligt indskud: "))
år = int(input("Indtast antallet af år: "))

# Beregner opsparingen.
opsparing = beregn_investering(initialbeløb, månedligt_indskud, år)

# Udskriver opsparingen pr. måned.
print("Måned\tOpsparing")
for måned, beløb in enumerate(opsparing):
  print(f"{måned + 1}\t{beløb:.2f}")
