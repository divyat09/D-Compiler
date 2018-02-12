.data
format_out: .asciz "%d\n"
format_in: .asciz "%d"
a: .long 0
c: .long 0
b: .long 0

.text
.globl _start
_start:
movl	$7,	%eax
movl	$7,	%edi
movl	$5,	%ebx
cmpl	%edi,%eax
je	label5
movl	%eax,	a
movl	%edi,	b
movl	%ebx,	c
call	foo
movl	$0,%ebx
movl	$1,%eax
int	$0x80
label5:

.type foo , @function
foo:
push	%ebp
mov	%esp,	%ebp
pushl	a
pushl	$format_out
call	printf
addl	$8,%esp
mov	%ebp,	%esp
pop	%ebp
movl	$0,%eax
ret
