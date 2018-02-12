.data
format_int: .asciz "%d\n"
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
