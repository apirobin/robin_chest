**Script by robinapi**

Version: 1.0

Start: 11.02.2025 12:24
Letzte Änderung: 11.02.2025 13:29 Uhr (FINAL)

Doc:
    Calculates the difference between the wished height and the total height of small and big chests.

    Args:
        smallChest (int): The number of small chests.
        bigChest (int): The number of big chests.
        wishedHeight (int): The desired height.

    Returns:
        int: The difference between the wished height and the total height.
             Returns the difference if it is greater than or equal to 1.
             Returns 0 if the difference is exactly 0.
             Returns 404 if the difference is negative.
             Returns -1 for any other case.


Ursprünglicher Auftrag:
Entwerfen Sie einen Algorithmus, um zu bestimmen, ob bei einer
eingegebenen Anzahl von kleinen und großen Kisten mit unterschiedlichen Höhen,
ein gewünschtes Kistenstapel gestapelt werden kann. Kleine Kisten haben die Höhe
1 und große Kisten haben die Höhe 5. Z. B.:
• Anzahl kleiner Kisten eingeben: 2
• Anzahl großer Kisten eingeben: 2
• Höhe des gewünschten Stapels eingeben: 11
• Ja, ein Stapel der Höhe 11 kann aus 2 großen und 1 kleinen KisteNein gebaut
werden.
Hinweis:
• Mit 3 kleinen Kisten und einer großen Kiste kann ein Kistenstapel der Höhe 8
gebaut werden.
• Mit 3 kleinen Kisten und einer großen Kiste kann kein Kistenstapel der Höhe 9
gebaut werden.
• Mit 3 kleinen Kisten und zwei großen Kisten kann ein Kistenstapel der Höhe 10
gebaut werden.
• Achtung: Mit 3 kleinen Kisten und zwei großen Kisten kann kein Kistenstapel der
Höhe 9 gebaut werden, obwohl alle Kisten zusammen die Höhe 13 ergeben.

© Robin S. 2025