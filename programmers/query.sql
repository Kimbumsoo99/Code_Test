-- 조건에 맞는 회원수 구하기
SELECT COUNT(USER_ID) AS USERS FROM USER_INFO WHERE JOINED LIKE "2021%" AND AGE <= 29 AND AGE >= 20

-- 가격이 제일 비싼 식품의 정보 출력하기
SELECT * FROM FOOD_PRODUCT WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)

-- 최대값 구하기
SELECT DATETIME AS 시간 FROM ANIMAL_INS WHERE DATETIME = (SELECT MAX(DATETIME) FROM ANIMAL_INS)