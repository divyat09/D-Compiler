.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
c: .long 0
b: .long 0
i: .long 0
j: .long 0
tmp1: .long 0
tmp3: .long 0
tmp2: .long 0

.text
.globl _start
_start:
main:
movl	$10,	%eax
movl	$0,	%edi
movl	%eax,	b
movl	%edi,	i
movl	b,	%eax
movl	tmp1,	%edi
cmpl	%edi,%eax
jne	L2
movl	$5,	%ebx
movl	%eax,	b
movl	%edi,	tmp1
movl	%ebx,	c
JMP	L1
L2:
movl	b,	%eax
movl	tmp2,	%edi
cmpl	%edi,%eax
jne	L3
movl	$1,	%ebx
movl	%eax,	b
movl	%edi,	tmp2
movl	%ebx,	j
JMP	L1
L3:
movl	b,	%eax
movl	%eax,	%edi
addl	$1,	%edi
movl	%edi,	%eax
L1:
mov	%ebp,	%esp
pop	%ebp
movl	$0,%eax
ret
