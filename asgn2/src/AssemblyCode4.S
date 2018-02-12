<<<<<<< HEAD
.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
a: .long 0
i: .long 0
A[i]: .long 0

.text
.globl _start
_start:
movl	$2,	%eax
movl	$1,	%edi
movl	%eax,	a
movl	%edi,	i
movl	a,	%eax
movl	A,	%edi
=======
>>>>>>> 069458aada1e7e2f41ef80a6e751d42830669c62
