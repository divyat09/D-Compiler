.data
a: .long 0
c: .long 0
b: .long 0

.text
.global _start
_start:
movl	$0x5,	%eax
movl	$0x2,	%edi
movl	%eax,	%ebx
addl	%edi,	%ebx
movl	%ebx,	(c)
movl	%eax,	(a)
movl	$0x9,	%edx
movl	c,	%ecx
movl	$0x4,	%eax
movl	$0x1,	%ebx
int	$0x80
movl    $0x1,%eax
int $0x80
