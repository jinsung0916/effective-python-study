# BETTER WAY 3 bytes와 str의 차이를 알아두라

"""
bytes -[decode]> str -[encode]> bytes
"""

a = b'h\x65llo' 
print(list(a))
print(a)

a = 'a\u0300 propos'
print(list(a))
print(a)

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str

    return value

print(to_str(b'foo'))
print(repr(to_str('bar')))
print(repr(to_str(b'\xed\x95\x9c'))) # UTF-8 에서 한글은 3바이트임

def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str

    return value

print(to_bytes(b'foo'))
print(repr(to_bytes('bar')))
print(repr(to_bytes('한')))

print(b'one' + b'two')
print('one' + 'two')

"""
print(b'one' + 'two') # TypeError: can't concat str to bytes
"""

assert b'red' > b'blue'
assert 'red' > 'blue'

"""
assert 'red' > b'blue' # TypeError: '>' not supported between instances of 'str' and 'bytes'
assert b'blue' < 'red' # TypeError: '<' not supported between instances of 'bytes' and 'str'
"""

print(b'red %s' % b'blue')
print('red %s' % 'blue')

"""
print(b'red %s' % 'blue') # TypeError: %b requires a bytes-like object, or an object that implements __bytes__, not 'str'
"""
print('red %s' % b'blue') # bytes 인스턴스의 __repr__ 을 호출한다.