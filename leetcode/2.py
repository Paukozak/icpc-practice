class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numero1= 0
        numero2= 0
        i=0
        p = l1
        while p:
            numero1 += p.val * (10**i)
            p = p.next
            i+=1
        i=0
        p = l2
        while p:
            numero2 += p.val * (10**i)
            p = p.next
            i+=1
        
        aux=numero1+numero2
        sal = ListNode(0)
        salida = sal #Creo una lista con el primer nodo en 0
        while aux != 0:
            nodonuevo = ListNode(aux % 10)  # último dígito
            salida.next = nodonuevo         # lo conecto
            salida = salida.next            # avanzo
            aux //= 10                 # quito el dígito ya usado
        if sal.next:
            return sal.next #Porque salida comienza con un nodo inicial 0, devuelvo lo que sigue al 0
        else:
            return sal
        