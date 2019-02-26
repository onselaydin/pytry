def clear(text):
    donustur =	{
    "&#252;": "ü", "&uuml;": "ü", "&Uuml;": "Ü", "&ucirc;": "û", "&#214;": "Ö", "&#199;": "Ç",
    "&#231;": "ç", "&ccedil;": "ç", "&Ccedil;": "Ç", "&#39;": "'", "&#246;": "ö", "&Ouml;": "Ö",
    "&ouml;": "ö", "&#220;": "Ü", "&acirc;": "â", "&ldquo;": "\"", "&rsquo;": "'", "&hellip;": "...",
    "&ocirc;": "ô", "&icirc;": "î", "Ý": "İ", "ý": "ı"
    }
    for i,j in donustur.items():
        a = text.find(i, 0, len(text))
        if a != -1:
            return text.replace(i,j)
        else:
            return text
