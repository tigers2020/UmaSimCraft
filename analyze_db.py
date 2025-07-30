#!/usr/bin/env python3
"""
db.sqlite3 파일 분석 스크립트
"""

import sqlite3
import os


def analyze_database():
    """데이터베이스 구조를 분석합니다."""

    if not os.path.exists("db.sqlite3"):
        print("❌ db.sqlite3 파일을 찾을 수 없습니다.")
        return

    try:
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()

        # 테이블 목록 조회
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        print("📊 db.sqlite3 데이터베이스 분석 결과")
        print("=" * 50)

        if not tables:
            print("❌ 테이블이 없습니다.")
            return

        print(f"📋 총 {len(tables)}개의 테이블이 있습니다:\n")

        for table in tables:
            table_name = table[0]
            print(f"🔍 테이블: {table_name}")
            print("-" * 30)

            # 테이블 스키마 조회
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()

            print("📝 컬럼 정보:")
            for col in columns:
                col_id, col_name, col_type, not_null, default_val, pk = col
                pk_mark = " 🔑" if pk else ""
                not_null_mark = " NOT NULL" if not_null else ""
                default_mark = f" DEFAULT {default_val}" if default_val else ""
                print(
                    f"  - {col_name} ({col_type}){not_null_mark}{default_mark}{pk_mark}"
                )

            # 레코드 수 조회
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"📊 레코드 수: {count:,}개")

            # 샘플 데이터 조회 (처음 3개)
            if count > 0:
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")
                sample_data = cursor.fetchall()
                print("📄 샘플 데이터:")
                for i, row in enumerate(sample_data, 1):
                    print(f"  {i}. {row}")

            print()

        conn.close()
        print("✅ 분석 완료!")

    except sqlite3.Error as e:
        print(f"❌ 데이터베이스 오류: {e}")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")


if __name__ == "__main__":
    analyze_database()
