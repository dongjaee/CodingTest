select concat('/home/grep/src/',a.BOARD_ID,'/',FILE_ID,FILE_NAME,FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD as a
join USED_GOODS_FILE as b on a.BOARD_ID=b.BOARD_ID
where a.VIEWS = (select max(VIEWS) from USED_GOODS_BOARD)
order by b.FILE_ID DESC