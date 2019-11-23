def removeDuplicates(S: str) -> str:
    st = []
    for c in S:
        if st and c == st[-1]:
            st.pop()
        else:
            st.append(c)
    return ''.join(st)


print(removeDuplicates('ABBCCCDEFA'))
