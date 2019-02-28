def clear(text):
    donustur =	{
    "&#252;": "ü", "&uuml;": "ü", "&Uuml;": "Ü", "&ucirc;": "û", "&#214;": "Ö", "&#199;": "Ç",
    "&#231;": "ç", "&ccedil;": "ç", "&Ccedil;": "Ç", "&#39;": "'", "&#246;": "ö", "&Ouml;": "Ö",
    "&ouml;": "ö", "&#220;": "Ü", "&acirc;": "â", "&ldquo;": "\"", "&rsquo;": "'", "&hellip;": "...",
    "&ocirc;": "ô", "&icirc;": "î", "Ý": "İ", "ý": "ı",
    "<h2>": "", "</h2>": "", "<p>": "", "</p>": "", "<strong>": "","</strong>": "", "<div>": "", "</div>": "", "<br>": "","<h4>": "",
    "</h4>": "", "</span>": "", "<span>": "", "&nbsp;": "", "<div class=""row"">": "",
    "<div class=""col-sm-4 mb10"">": "", "<td>": "", "</td>": "", "&rdquo;": """, "&lsquo;": """, "<tr>": "", "</tr>": "",
    "<table>": "", "</table>": "", "<a href>": "", "</a>": "", "<table class=""pd-table"">": "", "<span lang=""TR"">": "",
    "<p style=""margin - left:0in; margin - right:0in"">": "", "<em>": "", "</em>": "", "<p style=""margin - left:36.0pt"">": "",
    "<div style=\"margin - top:10px\">": "", "<li>": "", "</li>": ""
    }
    for i,j in donustur.items():
        a = text.find(i, 0, len(text))
        if a != -1:
            return text.replace(i,j)
        else:
            return text
