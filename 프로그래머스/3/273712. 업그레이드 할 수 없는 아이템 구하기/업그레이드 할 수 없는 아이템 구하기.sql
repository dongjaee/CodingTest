SELECT b.ITEM_ID, b.ITEM_NAME, b.RARITY
FROM ITEM_INFO b
LEFT JOIN ITEM_TREE t ON b.ITEM_ID = t.PARENT_ITEM_ID
WHERE t.PARENT_ITEM_ID IS NULL
ORDER BY b.ITEM_ID DESC;