.data
format_int: .asciz "%d\n"
a: .long 0
b: .long 0

.text
.globl _start
_start:
movl	$2,	%eax
movl	$7,	%edi
movl	%eax,	a
movl	%edi,	b
label2:
movl	a,	%eax
movl	b,	%edi
addl	%edi,	%eax
movl	%eax,	a
movl	%edi,	b
movl	a,	%eax
cmpl	$50,%eax
jle	label2
movl	%eax,	a
call	foo
movl	$0,%ebx
movl	$1,%eax
int	$0x80

.type foo , @function
foo:
push	%ebp
mov	%esp,	%ebp
pushl	a
pushl	$format_int
call	printf
mov	%ebp,	%esp
pop	%ebp
movl	$0,%eax
ret
