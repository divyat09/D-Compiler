.data
format_int: .asciz "%d\n"
a: .long 0
b: .long 0

.text
.globl _start
_start:
movl	$2,	%eax
label2:
movl	%eax,	a
movl	$7,	%eax
movl	a,	%edi
addl	%eax,	%edi
cmpl	%edi,%ebx
jle	label2
movl	%eax,	b
movl	%edi,	a
