class SGA:

    en_ = "a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z"
    sga_ = "ᔑ/ʖ/ᓵ/↸/ᒷ/⎓/⊣/⍑/╎/⋮/ꖌ/ꖎ/ᒲ/リ/𝙹/!¡/ᑑ/∷/ᓭ/ℸ ̣ /⚍/⍊/∴/ {X}/||/⨅"
    en_parsed = en_.split("/")
    sga_parsed = sga_.split("/")

    def encode(self, text: str):
        for L in text:
            if L in self.en_parsed:
                index_ = self.en_parsed.index(L)
                text = text.replace(
                    self.en_parsed[index_],
                    self.sga_parsed[index_]
                )
        return text.replace("{X}", "̇/")

    def decode(self, encoded_text: str):
        encoded_text = encoded_text.replace("̇/", "{X}")
        for x in self.sga_parsed:
            index_ = self.sga_parsed.index(x)
            encoded_text = encoded_text.replace(
                x, self.en_parsed[index_]
            )
        return encoded_text.capitalize()