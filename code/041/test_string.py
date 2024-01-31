def test_string(aa: int, bb: int, cc: int) -> str:
    return f"{aa:d} -" \
           f"{bb:d} - {cc:d}"
           
print(test_string(1, 2, 3))
