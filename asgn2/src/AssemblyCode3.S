.data
a: .long 0
c: .long 0
b: .long 0

.text
.global _main
_main:
movl	5,	%eax
movl	3,	%edi
movl	%eax,	%ebx
addl	%edi,	%ebx
movl	%ebx,	c
movl	%eax,	a
mov	5,%edx
mov	c%ecx
mov	1,%ebx
mov	$0x4,eax
int	$0x80