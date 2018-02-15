.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
i: .long 0
A: .zero 40

.text
.globl _start
_start:
movl	$0,	%eax
movl	%eax,	i
L2:
movl	i,	%eax
movl	$A,	%edi
movl	(%edi, %eax, 4),	%ebx
movl	%eax,	%ebx
movl	$A,	%esi
movl	i,	%ecx
movl	%ebx,	(%esi, %ecx, 4)
addl	$1,	%eax
movl	%eax,	i
movl	%edi,	A
movl	$A,	%eax
movl	i,	%edi
movl	%ebx,	(%eax, %edi, 4)
movl	i,	%eax
cmpl	$3,%eax
jl	L2
movl	%eax,	i
movl	$5,	%eax
cmpl	$-5,%eax
je	L8
call	power
L8:
movl	$0,%ebx
movl	$1,%eax
int	$0x80

.type power , @function
power:
push	%ebp
mov	%esp,	%ebp
movl	$0,	%eax
movl	%eax,	i
L12:
movl	$A,	%edi
movl	i,	%ebx
movl	(%edi, %ebx, 4),	%esi
pushl	%esi
pushl	$format_out
call	printf
addl	$8,%esp
addl	$1,	%ebx
movl	%edi,	A
movl	%ebx,	i
movl	A,	%eax
movl	i,	%edi
movl	%esi,	(%eax, %edi, 4)
movl	i,	%eax
cmpl	$3,%eax
jl	L12
mov	%ebp,	%esp
pop	%ebp
movl	$0,%eax
ret
