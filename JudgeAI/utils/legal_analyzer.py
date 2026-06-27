
import re

def extract_date(text):

    patterns = [

        r"date of judgment\s*([0-9]{2}/[0-9]{2}/[0-9]{4})",

        r"dated\s*([0-9]{2}[./-][0-9]{2}[./-][0-9]{4})",

        r"judgment dated\s*([0-9]{2}[./-][0-9]{2}[./-][0-9]{4})"

    ]

    for pattern in patterns:

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1)

    return "Not Found"

def extract_court(text):
    for p in [r"IN THE\s+(.+?COURT.+)",r"(supreme court of india)",r"([A-Za-z ]+high court)"]:
        m=re.search(p,text,re.I)
        if m:
            return m.group(1) if m.lastindex else m.group(0)
    return "Not Found"

def extract_case_type(text):
    for t in ["Civil Appeal","Criminal Appeal","Writ Petition","Civil Appellate Jurisdiction"]:
        if re.search(t,text,re.I):
            return t
    return "Not Found"

def extract_case_number(text):
    """
    Extract Case Number
    """

    patterns = [

        r"(Civil Appeal\s*(?:Number|No\.?)\s*[\w/\- ]+)",

        r"(Criminal Appeal\s*(?:Number|No\.?)\s*[\w/\- ]+)",

        r"(Appeal\s*(?:Number|No\.?)\s*[\w/\- ]+)",

        r"(Civil Appeal Number\s*[\w/\- ]+)",

        r"(Criminal Appeal Number\s*[\w/\- ]+)",

        r"(Writ Petition\s*(?:Number|No\.?)\s*[\w/\- ]+)",

        r"(SLP\s*(?:No\.?)\s*[\w/\- ]+)",

        r"(Special Leave Petition\s*(?:No\.?)\s*[\w/\- ]+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            return " ".join(
                match.group(1).split()
            )

    return "Not Found"

def extract_bench(text):
    """
    Extract Bench / Judges
    """

    patterns = [

        r"bench\s+(.*?)\s+citation",

        r"coram\s*:(.*?)\n",

        r"before\s*:(.*?)\n"

    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:

            bench_text = match.group(1)

            bench_text = re.sub(
                r"\bbench\b",
                "",
                bench_text,
                flags=re.IGNORECASE
            )

            bench_text = re.sub(
                r"\s+",
                " ",
                bench_text
            )

            judges = re.split(
                r",(?=\s*[A-Za-z])",
                bench_text
            )

            judges = [
                judge.strip()
                for judge in judges
                if judge.strip()
            ]

            return judges

    return []
def extract_citation(text):
    m=re.search(r"citation\s+(.*?)\s+act",text,re.I|re.S)
    return " ".join(m.group(1).split()) if m else "Not Found"

def extract_acts(text):
    """
    Extract all Acts, Codes and Rules mentioned in the judgment.
    """

    patterns = [

        r"([A-Z][A-Za-z ,&()\-]+? Act(?:,?\s*\d{4})?)",

        r"([A-Z][A-Za-z ,&()\-]+? Code)",

        r"([A-Z][A-Za-z ,&()\-]+? Rules(?:,?\s*\d{4})?)",

        r"(Indian Penal Code)",

        r"(Code of Criminal Procedure)",

        r"(Code of Civil Procedure)",

        r"(Constitution of India)",

        r"(IPC)",

        r"(CrPC)",

        r"(CPC)"

    ]

    acts = []

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text,
            re.IGNORECASE
        )

        for match in matches:

            act = " ".join(match.split())

            if act not in acts:
                acts.append(act)

    return acts
def extract_sections(text):
    """
    Extract Sections, Articles, Rules and Orders
    """

    patterns = [

        r"section\s+\d+[A-Za-z()]*",

        r"sections\s+\d+[A-Za-z(),\s]*",

        r"article\s+\d+[A-Za-z()]*",

        r"rule\s+\d+[A-Za-z()]*",

        r"rules\s+\d+[A-Za-z(),\s]*",

        r"order\s+\d+\s+rule\s+\d+",

        r"ipc\s+\d+",

        r"crpc\s+\d+",

        r"cpc\s+\d+"

    ]

    sections = []

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text,
            re.IGNORECASE
        )

        for match in matches:

            value = " ".join(match.split())

            if value not in sections:

                sections.append(value.title())

    return sections 

def extract_headnote(text):
    """
    Extract Headnote
    """

    patterns = [

        r"headnote(.*?)(judgment)",

        r"headnote(.*?)(civil appellate jurisdiction)",

        r"headnote(.*?)(criminal appellate jurisdiction)",

        r"headnote(.*?)(the judgment of the court)"

    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE | re.DOTALL
        )

        if match:

            headnote = " ".join(
                match.group(1).split()
            )

            return headnote

    return "Not Found"
def extract_final_decision(text):
    """
    Extract Final Decision
    """

    decision_keywords = {

        "appeal dismissed": "Appeal Dismissed",

        "appeal allowed": "Appeal Allowed",

        "appeal succeeds": "Appeal Allowed",

        "appeal fails": "Appeal Dismissed",

        "petition dismissed": "Petition Dismissed",

        "petition allowed": "Petition Allowed",

        "petition succeeds": "Petition Allowed",

        "petition fails": "Petition Dismissed",

        "writ petition allowed": "Writ Petition Allowed",

        "writ petition dismissed": "Writ Petition Dismissed",

        "matter remanded": "Matter Remanded",

        "judgment affirmed": "Judgment Affirmed",

        "judgment set aside": "Judgment Set Aside",

        "disposed of": "Disposed",

        "order accordingly": "Order Passed"

    }

    last_text = text[-5000:].lower()

    for keyword, result in decision_keywords.items():

        if keyword in last_text:

            return result

    return "Not Found"

def extract_legal_issue(text):
    """
    Extract Legal Issue
    """

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text
    )

    keywords = [

        "whether",

        "question",

        "issue",

        "dispute",

        "challenge",

        "validity",

        "jurisdiction"

    ]

    issues = []

    for sentence in sentences:

        if any(
            keyword in sentence.lower()
            for keyword in keywords
        ):

            issues.append(
                sentence.strip()
            )

    if issues:

        return " ".join(
            issues[:2]
        )

    return "Not Found"
def analyze_judgment(text):
    return {
        "date":extract_date(text),
        "court":extract_court(text),
        "case_type":extract_case_type(text),
        "case_number":extract_case_number(text),
        "bench":extract_bench(text),
        "citation":extract_citation(text),
        "acts":extract_acts(text),
        "sections":extract_sections(text),
        "headnote":extract_headnote(text),
        "legal_issue":extract_legal_issue(text),
        "final_decision":extract_final_decision(text)
    }
