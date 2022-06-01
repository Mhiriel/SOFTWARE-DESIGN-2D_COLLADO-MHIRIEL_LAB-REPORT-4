Find-Max(A, i, length)
    If i < length Then
        Return Max(A[i], Find-Max(A, i+1, length))
    Else
        Return -Infinity
    End If
