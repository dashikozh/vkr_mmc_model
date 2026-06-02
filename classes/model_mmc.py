import math
class ModelMMC:
    
    def __init__(self, lam, mu, c):
        """
        Конструктор класса
        λ - интенсивность поступления заявок
        μ - интенсивность обслуживания
        c - количество серверов
        """
        self.lam = lam
        self.mu  = mu
        self.c   = c


    def is_valid(self):
        # μ должна быть больше λ
        return self.mu > self.lam

    def mmc(self):
        
        result = {
            'lam': self.lam,
            'mu':  self.mu,
            'c':   self.c,
            'models': "mmc"
        }

        if not self.is_valid():
            result['log'] = '<span class="red">Значение <b>µ</b> должно быть больше <b>λ</b></span>'
            return result

        try:
            # Коэффициент использования серверов: U = λ / (c × µ)
            U  = self.lam / (self.c * self.mu)
            # Вероятность того, что система не занята
            U_pow_c = U ** self.c # возводим в степень
            fact_c  = math.factorial(self.c) # факториал
            P0 = U_pow_c / (fact_c * (1 - U)) # итоговое выражение
            # Среднее количество запросов в системе: L = (λ / (c ×(µ — λ)))
            L  = (self.lam / (self.c * (self.mu - self.lam)))
            # Среднее время, которое запрос проводит в системе: W = 1 / (c × (µ — λ))
            W  = 1 / (self.c * (self.mu - self.lam))
        
            result.update({
                'U':    f"{U:.3f}",
                'P0':   f"{P0:.3f}",
                'L':    f"{L:.3f}",
                'W':    f"{W:.3f}",
                'state': 'true',
                'log': '<span class="green">Данные успешно рассчитаны</span>'
            })
            return result

        except OverflowError:
            result['log'] = '<span class="red">Ошибка: слишком большое значение "c (количество серверов)"</span>'
        
