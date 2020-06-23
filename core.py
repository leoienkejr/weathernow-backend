def sanitize_query(query):
    allowed_chars = 'qwertyuiopasdfghjklçzxcvbnm'
    allowed_chars += allowed_chars.upper()
    allowed_chars += '0123456789'
    allowed_chars += ',;-'
    allowed_chars = set(allowed_chars)

    if len(query) > 128:
        query = query[:128]

    sanitized_query = ''.join([char for char in query
                               if char in allowed_chars])
    return sanitized_query


if __name__ == '__main__':
    pass
