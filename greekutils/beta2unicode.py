from .trie import Trie


def generate_trie():
    t = Trie()

    t.add("#", "\u0374")

    t.add("*A", "\u0391")
    t.add("*B", "\u0392")
    t.add("*G", "\u0393")
    t.add("*D", "\u0394")
    t.add("*E", "\u0395")
    t.add("*Z", "\u0396")
    t.add("*H", "\u0397")
    t.add("*Q", "\u0398")
    t.add("*I", "\u0399")
    t.add("*K", "\u039A")
    t.add("*L", "\u039B")
    t.add("*M", "\u039C")
    t.add("*N", "\u039D")
    t.add("*C", "\u039E")
    t.add("*O", "\u039F")
    t.add("*P", "\u03A0")
    t.add("*R", "\u03A1")
    # U+03A2
    t.add("*S", "\u03A3")
    t.add("*T", "\u03A4")
    t.add("*U", "\u03A5")
    t.add("*F", "\u03A6")
    t.add("*X", "\u03A7")
    t.add("*Y", "\u03A8")
    t.add("*W", "\u03A9")
    # U+03AA thru U+03B0
    t.add("A", "\u03B1")
    t.add("B", "\u03B2")
    t.add("G", "\u03B3")
    t.add("D", "\u03B4")
    t.add("E", "\u03B5")
    t.add("Z", "\u03B6")
    t.add("H", "\u03B7")
    t.add("Q", "\u03B8")
    t.add("I", "\u03B9")
    t.add("K", "\u03BA")
    t.add("L", "\u03BB")
    t.add("M", "\u03BC")
    t.add("N", "\u03BD")
    t.add("C", "\u03BE")
    t.add("O", "\u03BF")
    t.add("P", "\u03C0")
    t.add("R", "\u03C1")
    t.add("S\n", "\u03C2")
    t.add("S,", "\u03C2,")
    t.add("S.", "\u03C2.")
    t.add("S:", "\u03C2:")
    t.add("S;", "\u03C2;")
    t.add("S]", "\u03C2]")
    t.add("S@", "\u03C2@")
    t.add("S_", "\u03C2_")
    t.add("S", "\u03C3")
    t.add("T", "\u03C4")
    t.add("U", "\u03C5")
    t.add("F", "\u03C6")
    t.add("X", "\u03C7")
    t.add("Y", "\u03C8")
    t.add("W", "\u03C9")
    t.add("I+", "\u03CA")
    t.add("U+", "\u03CB")
    # U+03CC thru U+03D9
    t.add("*V", "\u03DA")
    t.add("V", "\u03DB")

    t.add("A)", "\u1F00")
    t.add("A(", "\u1F01")
    t.add("A)\\", "\u1F02")
    t.add("A(\\", "\u1F03")
    t.add("A)/", "\u1F04")
    t.add("A(/", "\u1F05")
    t.add("A)=", "\u1F06")
    t.add("A(=", "\u1F07")
    t.add("*A)", "\u1F08")
    t.add("*)A", "\u1F08")
    t.add("*A(", "\u1F09")
    t.add("*(A", "\u1F09")
    # U+1F0A
    t.add("*(\A", "\u1F0B")
    t.add("*A)/", "\u1F0C")
    t.add("*)/A", "\u1F0C")
    # U+1F0D
    t.add("*A)=", "\u1F0E")
    t.add("*)=A", "\u1F0E")
    t.add("*A(=", "\u1F0F")  # @@@ check these three
    t.add("*A(/", "\u1F0F")  # @@@ check these three
    t.add("*(/A", "\u1F0F")  # @@@ check these three
    t.add("E)", "\u1F10")
    t.add("E(", "\u1F11")
    t.add("E)\\", "\u1F12")
    t.add("E(\\", "\u1F13")
    t.add("E)/", "\u1F14")
    t.add("E(/", "\u1F15")
    # U+1F16 and U+1F17
    t.add("*E)", "\u1F18")
    t.add("*)E", "\u1F18")
    t.add("*E(", "\u1F19")
    t.add("*(E", "\u1F19")
    # U+1F1A
    t.add("*(\E", "\u1F1B")
    t.add("*E)/", "\u1F1C")
    t.add("*)/E", "\u1F1C")
    t.add("*E(/", "\u1F1D")
    t.add("*(/E", "\u1F1D")
    # U+1F1E and U+1F1F
    t.add("H)", "\u1F20")
    t.add("H(", "\u1F21")
    t.add("H)\\", "\u1F22")
    t.add("H(\\", "\u1F23")
    t.add("H)/", "\u1F24")
    t.add("H(/", "\u1F25")
    t.add("H)=", "\u1F26")
    t.add("H(=", "\u1F27")
    t.add("*H)", "\u1F28")
    t.add("*)H", "\u1F28")
    t.add("*H(", "\u1F29")
    t.add("*(H", "\u1F29")
    t.add("*H)\\", "\u1F2A")
    t.add(")\\*H", "\u1F2A")
    t.add("*)\\H", "\u1F2A")
    # U+1F2B
    t.add("*H)/", "\u1F2C")
    t.add("*)/H", "\u1F2C")
    # U+1F2D
    t.add("*)=H", "\u1F2E")
    t.add("(/*H", "\u1F2F")
    t.add("*(/H", "\u1F2F")
    t.add("I)", "\u1F30")
    t.add("I(", "\u1F31")
    t.add("I)\\", "\u1F32")
    t.add("I(\\", "\u1F33")
    t.add("I)/", "\u1F34")
    t.add("I(/", "\u1F35")
    t.add("I)=", "\u1F36")
    t.add("I(=", "\u1F37")
    t.add("*I)", "\u1F38")
    t.add("*)I", "\u1F38")
    t.add("*I(", "\u1F39")
    t.add("*(I", "\u1F39")
    # U+1F3A and U+1F3B
    t.add("*I)/", "\u1F3C")
    t.add("*)/I", "\u1F3C")
    # U+1F3D and U+1F3E
    t.add("*I(/", "\u1F3F")
    t.add("*(/I", "\u1F3F")
    t.add("O)", "\u1F40")
    t.add("O(", "\u1F41")
    t.add("O)\\", "\u1F42")
    t.add("O(\\", "\u1F43")
    t.add("O)/", "\u1F44")
    t.add("O(/", "\u1F45")
    # U+1F46 and U+1F47
    t.add("*O)", "\u1F48")
    t.add("*)O", "\u1F48")
    t.add("*O(", "\u1F49")
    t.add("*(O", "\u1F49")
    # U+1F4A
    t.add("*(\O", "\u1F4B")
    t.add("*O)/", "\u1F4C")
    t.add("*)/O", "\u1F4C")
    # U+1F4D and U+1F4E
    t.add("*O(/", "\u1F4F")
    t.add("*(/O", "\u1F4F")
    t.add("U)", "\u1F50")
    t.add("U(", "\u1F51")
    t.add("U)\\", "\u1F52")
    t.add("U(\\", "\u1F53")
    t.add("U)/", "\u1F54")
    t.add("U(/", "\u1F55")
    t.add("U)=", "\u1F56")
    t.add("U(=", "\u1F57")
    # U+1F58
    t.add("*U(", "\u1F59")
    t.add("*(U", "\u1F59")
    # U+1F5A thru U+1F5C
    t.add("*(/U", "\u1F5D")
    # U+1F5E
    t.add("*(=U", "\u1F5F")
    t.add("W)", "\u1F60")
    t.add("W(", "\u1F61")
    t.add("W)\\", "\u1F62")
    t.add("W(\\", "\u1F63")
    t.add("W)/", "\u1F64")
    t.add("W(/", "\u1F65")
    t.add("W)=", "\u1F66")
    t.add("W(=", "\u1F67")
    t.add("*W)", "\u1F68")
    t.add("*W(", "\u1F69")
    t.add("*(W", "\u1F69")
    # U+1F6A and U+1F6B
    t.add("*W)/", "\u1F6C")
    t.add("*)/W", "\u1F6C")
    # U+1F6D
    t.add("*W)=", "\u1F6E")
    t.add("*)=W", "\u1F6E")
    t.add("*W(/", "\u1F6F")  # @@@
    t.add("*(/W", "\u1F6F")  # @@@
    t.add("*W(=", "\u1F6F")  # @@@
    t.add("*(=W", "\u1F6F")  # @@@
    t.add("A\\", "\u1F70")
    t.add("A/", "\u1F71")
    t.add("E\\", "\u1F72")
    t.add("E/", "\u1F73")
    t.add("H\\", "\u1F74")
    t.add("H/", "\u1F75")
    t.add("I\\", "\u1F76")
    t.add("I/", "\u1F77")
    t.add("O\\", "\u1F78")
    t.add("O/", "\u1F79")
    t.add("U\\", "\u1F7A")
    t.add("U/", "\u1F7B")
    t.add("W\\", "\u1F7C")
    t.add("W/", "\u1F7D")
    # U+1F7E and U+1F7F
    t.add("A)|", "\u1F80")
    # U+1F81 thru U+1F83
    t.add("A)/|", "\u1F84")
    t.add("A(/|", "\u1F85")
    t.add("A)=|", "\u1F86")
    # U+1F87
    t.add("*A)|", "\u1F88")
    # U+1F89 thru U+1F8D
    t.add("*A)=|", "\u1F8E")
    # U+1F8F
    t.add("H)|", "\u1F90")
    t.add("H(|", "\u1F91")
    # U+1F92 and U+1F93
    t.add("H)/|", "\u1F94")
    # U+1F95
    t.add("H)=|", "\u1F96")
    t.add("H(=|", "\u1F97")
    # U+1F98 thru U+1F9F
    t.add("W)|", "\u1FA0")
    # U+1FA1 thru U+1FA3
    t.add("W)/|", "\u1FA4")
    # U+1FA5 and U+1FA6
    t.add("W(=|", "\u1FA7")
    # U+1FA8 thru U+1FAB
    t.add("*W)/|", "\u1FAC")
    # U+1FAD thru U+1FB2
    t.add("A|", "\u1FB3")
    t.add("A/|", "\u1FB4")
    # U+1FB5
    t.add("A=", "\u1FB6")
    t.add("A=|", "\u1FB7")
    # U+1FB8 thru U+1FC2
    t.add("H|", "\u1FC3")
    t.add("H/|", "\u1FC4")
    # U+1FC5
    t.add("H=", "\u1FC6")
    t.add("H=|", "\u1FC7")
    # U+1FC8 thru U+1FD1
    t.add("I\\+", "\u1FD2")
    t.add("I/+", "\u1FD3")
    t.add("I+/", "\u1FD3")
    t.add("I=", "\u1FD6")
    # U+1FD7 thru U+1FE1
    t.add("U\\+", "\u1FE2")
    t.add("U/+", "\u1FE3")
    t.add("R(", "\u1FE4")
    # U+1FE5
    t.add("U=", "\u1FE6")
    # U+1FE7 thru U+1FEB
    t.add("*R(", "\u1FEC")
    t.add("*(R", "\u1FEC")
    # U+1FED thru U+1FF2
    t.add("W|", "\u1FF3")
    t.add("W|/", "\u1FF4")
    t.add("W/|", "\u1FF4")
    # U+1FF5
    t.add("W=", "\u1FF6")
    t.add("W=|", "\u1FF7")
    # U+1FF8 thru U+1FFF

    t.add("~", "~")
    t.add("-", "-")

    t.add("(null)", "(null)")
    t.add("&", "&")

    t.add("0", "0")
    t.add("1", "1")
    t.add("2", "2")
    t.add("3", "3")
    t.add("4", "4")
    t.add("5", "5")
    t.add("6", "6")
    t.add("7", "7")
    t.add("8", "8")
    t.add("9", "9")

    t.add("@", "@")
    t.add("$", "$")

    t.add(" ", " ")

    t.add(".", ".")
    t.add(",", ",")
    t.add("'", "'")
    t.add(":", ":")
    t.add(";", ";")
    t.add("_", "_")

    t.add("[", "[")
    t.add("]", "]")

    t.add("\n", "")

    return t


beta2unicodeTrie = generate_trie()


def convert(input_string):
    output_string = ""
    consumed_string = ""
    input_left = input_string
    while input_left:
        consumed, output, input_left = beta2unicodeTrie.find_prefix(input_left)
        consumed_string += consumed
        if not output:
            raise KeyError(
                "attempted to convert {} "
                "but could only convert {} to {} leaving {}".format(
                    input_string, consumed_string, output_string, input_left
                )
            )
        output_string += output
    return output_string
