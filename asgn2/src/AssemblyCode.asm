.data
a: DW 0
c: DW 0
t5: DW 0
t2: DW 0
t3: DW 0
t1: DW 0

.text
.global _main
_main:
movl	3,	%eax
subl	1,	%eax
movl	5,	%edi
movl	%edi,	%ebx
mull	%eax,	%ebx
movl	%eax,	t1
movl	%edi,	%eax
idiv	%ebx
movl	%ebx,	t2
movl	%eax,	t3
mov	5%edx
mov	t3%ecx
mov	1,%ebx
mov	$0x4,eax
int	$0x80
movl	t3,	%eax
movl	%eax,	%ebx
addl	2,	%ebx
movl	c,	%esi
movl	%esi,	%ebx
addl	6,	%ebx
