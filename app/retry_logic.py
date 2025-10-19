# def is_section_valid(extracted_data, min_required=2):
#     valid_sections = {}

#     for section, params in extracted_data.items():
#         filled = [v for v in params.values() if v]
#         if len(filled) >= min_required:
#             valid_sections[section] = params
#         else:
#             print(f"⚠️ Retrying section '{section}' due to insufficient data.")
#     return valid_sections

def is_section_valid(extracted_data: dict, min_required_per_section: int = 2) -> bool:
    """
    Returns True if **every** section has at least min_required_per_section parameters filled (non‑null).
    """
    for section, params in extracted_data.items():
        filled = sum(1 for v in params.values() if v)
        if filled < min_required_per_section:
            return False
    return True
