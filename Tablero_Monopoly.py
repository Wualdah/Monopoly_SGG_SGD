import Datos_monoply
def taulellDibuixar():
    global jugadors

    # Definir el text que surt a cada casella del joc
    t = []
    for cntCasella in range(0, 54):
        txtCasella = " "
        jugadorsCasella = 0

        # Posar la lletra que correspon el jugador que hi ha a la casella (si n'hi ha)
        for cntJugador in range(0, len(jugadors)):
            if jugadors[cntJugador][idxPosicio] == cntCasella:
                jugadorsCasella = jugadorsCasella + 1
                color = jugadors[cntJugador][idxColor]
                if color == "Verda":
                    txtCasella = "D"
                else:
                    txtCasella = color[0]

        # Si hi ha més d'un jugador apareix el número de jugadors
        if jugadorsCasella > 1:
            txtCasella = str(jugadorsCasella)

        t.append(txtCasella)

    print(f"""
    +------+------+------+------+------+------+------+------+
    |00   {t[0]}|01   {t[1]}|02   {t[2]}|03   {t[3]}|04   {t[4]}|05*  {t[5]}|06P  {t[6]}|07   {t[7]}|
    +------+------+------+------+------+------+------+------+
    |25*  {t[25]}|26   {t[26]}|27   {t[27]}|28   {t[28]}|29U  {t[29]}|30*  {t[30]}|31   {t[31]}|08   {t[8]}|
    +------+------+------+------+------+------+------+------+
    |24D  {t[24]}|43   {t[43]}|44   {t[44]}|45   {t[45]}|46*  {t[46]}|47   {t[47]}|32   {t[32]}|09*  {t[9]}|
    +------+------+------+------+------+------+------+------+
    |23   {t[23]}|42   {t[42]}|53     LaOca       {t[53]}|48   {t[48]}|33   {t[33]}|10D  {t[10]}|
    +------+------+------+------+------+------+------+------+
    |22   {t[22]}|41*  {t[41]}|52C  {t[52]}|51   {t[51]}|50   {t[50]}|49   {t[49]}|34*  {t[34]}|11   {t[11]}|
    +------+------+------+------+------+------+------+------+
    |21*  {t[21]}|40   {t[40]}|39   {t[39]}|38L  {t[38]}|37*  {t[37]}|36   {t[36]}|35   {t[35]}|12   {t[12]}|
    +------+------+------+------+------+------+------+------+
    |20   {t[20]}|19P  {t[19]}|18   {t[18]}|17H  {t[17]}|16*  {t[16]}|15   {t[15]}|14   {t[14]}|13   {t[13]}|
    +------+------+------+------+------+------+------+------+
""")