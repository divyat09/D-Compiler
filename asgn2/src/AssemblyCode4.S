.data
format_int: .asciz "%d\n"
a: .long 0
i: .long 0
A: .zeros 40

.text
.globl _start
_start:
movl	$2,	%eax
movl	$1,	%edi
movl	A,	%ebx
movl	(%ebx, %edi, 4),	%esi
movl	%eax,	%esi
addl	$5,	%esi
movl	%eax,	a
movl	%edi,	i
movl	%ebx,	A
imul	$2,	%esi
label4:
cmpl	$500,%esi
jle	label4
call	Neg
movl	$0,%ebx
movl	$1,%eax
int	$0x80

.type Neg , @function
Neg:
push	%ebp
mov	%esp,	%ebp
pushl	%esi
pushl	$format_int
call	printf
imul	$-1,	%esi
pushl	%esi
pushl	$format_int
call	printf
mov	%ebp,	%esp
pop	%ebp
movl	$0,%eax
ret
