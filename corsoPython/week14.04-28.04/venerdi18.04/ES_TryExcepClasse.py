class GestoreErrori:
  @staticmethod
  def gestisci(e: Exception):
    if isinstance(e, IndexError):
      print("Errore di indice (LookupError):", e)
    elif isinstance(e, KeyError):
      print("Errore di chiave (LookupError):", e)
    elif isinstance(e, FileNotFoundError):
      print("File non trovato (OSError):", e)
    elif isinstance(e, PermissionError):
      print("Permessi insufficienti (OSError):", e)
    elif isinstance(e, ValueError):
      print("Conversione non valida (ValueError):", e)
    elif isinstance(e, TypeError):
      print("Tipo dati non compatibile (TypeError):", e)
    elif isinstance(e, ZeroDivisionError):
      print("Divisione per zero non permessa (ArithmeticError):", e)
    else:
      print("Errore imprevisto:", e)



def esempio():
  try:
    dizionario = {"a": 1}
    print(dizionario["b"])  # KeyError
  except Exception as e:
    GestoreErrori.gestisci(e)

esempio()
